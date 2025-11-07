create_graph <- function(num_vertices) {
  graph <- lapply(1:num_vertices, function(i) vector("integer"))
  names(graph) <- 1:num_vertices
  return(graph)
}

add_edge <- function(graph, u, v) {
  graph[[as.character(u)]] <- unique(c(graph[[as.character(u)]], v))
  graph[[as.character(v)]] <- unique(c(graph[[as.character(v)]], u))
  return(graph)
}

graph_adj_list <- create_graph(5)
print("Initial Adjacency List:")
print(graph_adj_list)

graph_adj_list <- add_edge(graph_adj_list, 1, 2)
graph_adj_list <- add_edge(graph_adj_list, 1, 3)
graph_adj_list <- add_edge(graph_adj_list, 2, 4)
graph_adj_list <- add_edge(graph_adj_list, 3, 4)
graph_adj_list <- add_edge(graph_adj_list, 3, 5)

print("Adjacency List after adding edges:")
print(graph_adj_list)

dfs_util <- function(u, graph, visited) {
  visited[u] <- TRUE
  cat(u, " ")
  for (v in graph[[as.character(u)]]) {
    if (!visited[v]) {
      visited <- dfs_util(v, graph, visited)
    }
  }
  return(visited)
}

dfs_traversal <- function(graph, start_vertex) {
  num_vertices <- length(graph)
  visited <- rep(FALSE, num_vertices)
  names(visited) <- 1:num_vertices
  
  cat("\nDFS Traversal starting from vertex", start_vertex, ":\n")
  dfs_util(start_vertex, graph, visited)
  cat("\n")
}

dfs_traversal(graph_adj_list, start_vertex = 1)
