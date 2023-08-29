from pygraph.classes.digraph import digraph
from connector import hiveConnector


class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

    def page_rank(self):
        #  先将图中没有出链的节点改为对所有节点都有出链
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank

            print("This is NO.%s iteration" % (i + 1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank


if __name__ == '__main__':
    conn = hiveConnector.getConnection()
    cursor = conn.cursor()
    sql_query = "select task_id,task_pid from xxx.ods_edw074_task_dependency_df where pt_d = '${ptdparam}' group by task_id,task_pid"
    cursor.execute(sql_query)
    dataList=cursor.fetchall()
    cursor.close()
    conn.close()



    conn_3 = hiveConnector.getConnection()
    cursor_3 = conn_3.cursor()
    sql_query_3 = '''select a.task_pid,0 from (select * from xxx.ods_edw074_task_dependency_df where pt_d = '${ptdparam}') a
                    left join (select * from xxxx.ods_edw074_task_dependency_df where pt_d = '${ptdparam}') b on a.task_pid =b.task_id
                    where b.task_pid is null and a.task_pid !=0
                    group by a.task_pid,b.task_pid'''
    cursor_3.execute(sql_query_3)
    dataList_3=cursor_3.fetchall()
    cursor_3.close()
    conn_3.close()

    task_id_set = set()

    for data in dataList:
        task_id_set.add(data[0])
    task_id_set.add(0)

    for data in dataList_3:
        task_id_set.add(data[0])

    dg = digraph()
    dg.add_nodes(task_id_set)

    for data in dataList:
        dg.add_edge(data)


    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    insert_sql =" insert overwrite table xxx.task_down_dependency_core_tmp  partition(pt_d = '${ptdparam}') values"
    for i,task_id in enumerate(task_id_set):
        rank = round((page_ranks.get(task_id) * 10000),2)
        value = "({},{})".format(task_id,rank)
        insert_sql = insert_sql + value
        if(i!=(len(task_id_set)-1)):
            insert_sql = insert_sql + ","
    conn_2 = hiveConnector.getConnection()
    cursor_2 = conn_2.cursor()
    cursor_2.execute(insert_sql)
    cursor_2.close()
    conn_2.close()
