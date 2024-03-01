# # import osmnx as ox
# # from xml.dom import minidom

# # osmFile="data/quan1.osm"
# # filePathML="data/map1.graphml"

# # def generateGraphML(osmFile,filePathML):
# #     multiGraph = ox.graph_from_file(osmFile,True,True,True)
# #     ox.save_graphml(multiGraph, filePathML)

# # def parseXML(graphMLFile):
# #     print("Called")
# #     xmldoc = minidom.parse(graphMLFile)
# #     return xmldoc


# import networkx as nx
# import osmnx as ox

# ox.settings.use_cache = True



# # lưu biểu đồ vào đĩa dưới dạng tệp .osm xml
# ox.settings.all_oneway = True
# ox.settings.log_console = True
# G = ox.graph_from_place("Quận tân bình, Thành phố HỒ CHÍ MINH, VIETNAM", network_type="bike")
# ox.io.save_graph_xml(G, filepath="./data/quantanbinh.osm")
# ox.io.save_graphml(G, filepath="./data/quantanbinh.graphml")



# # tính toán tốc độ biên (lái xe) và tính thời gian di chuyển biên
# G = ox.speed.add_edge_speeds(G)
# G = ox.speed.add_edge_travel_times(G)

# # có thể chuyển đổi MultiDiGraph sang/từ GeoPandas GeoDataFrames
# gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(G)
# G = ox.utils_graph.graph_from_gdfs(gdf_nodes, gdf_edges, graph_attrs=G.graph)

# # chuyển đổi MultiDiGraph sang DiGraph để sử dụng hàm nx.betweenness_centrality
# # chọn giữa các cạnh song song bằng cách giảm thiểu giá trị thuộc tính travel_time
# D = ox.utils_graph.get_digraph(G, weight="travel_time")

# # tính toán độ trung tâm của nút, tính theo thời gian di chuyển
# bc = nx.betweenness_centrality(D, weight="travel_time", normalized=True)
# nx.set_node_attributes(G, values=bc, name="bc")

# # vẽ biểu đồ, tô màu các nút theo tính trung tâm giữa
# nc = ox.plot.get_node_colors_by_attr(G, "bc", cmap="plasma")
# fig, ax = ox.plot.plot_graph(
#     G, bgcolor="k", node_color=nc, node_size=50, edge_linewidth=2, edge_color="#333333"
# )

# # # lưu biểu đồ dưới dạng tệp địa lý hoặc tệp graphml
# # ox.io.save_graph_xml(G, filepath="./data/quan1.osm")
# # ox.io.save_graphml(G, filepath="./data/quan1.graphml")