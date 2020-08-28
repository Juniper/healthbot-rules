def neighbor(neighbor_list,peer_state, **kwargs):
    if peer_state in neighbor_list:
        return 1
    else:
        return 0
