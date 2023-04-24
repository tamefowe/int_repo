import graph
import linked_list
import Tree
import character_string


def prefix_suffix(s):
    n = len(s)
    for i in range(n // 2, 0, -1):
        prefix = s[:i]
        suffix = s[n-i:]
        print(f"prefix: {prefix} -- suffix: {suffix}")
        if prefix == suffix:
            return True
    return False


def main():
    # graph.graph_search()
    # graph.has_path()
    # graph.construct_graph()
    # graph.connected_components_count()
    # graph.largest_component()
    # graph.shortest_path()
    # graph.island_count()
    # graph.minimum_island()
    # graph.course_schedule()
    # s = 'sdklklksdk'; prefix_suffix(s)
    # linked_list.run_zipper_lists()
    # linked_list.run_merge_lists()
    # linked_list.run_longest_streak()
    # linked_list.run_remove_node()
    # linked_list.run_create_linked_list()
    # linked_list.run_add_lists()
    # Tree.run_bottom_right_value()
    # Tree.run_all_tree_paths()
    # character_string.run_uncompress()
    # character_string.run_compress()
    # character_string.run_most_frequent_char()
    # character_string.run_decompress_braces()
    # character_string.run_nesting_score()
    # character_string.run_lowest_common_ancestor()
    # character_string.run_lefty_nodes()
    character_string.run_tolerant_teams()


if __name__ == '__main__':
    main()
