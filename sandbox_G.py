def compile_project(graph, query, compiled):
    compiled_list = []

    def helper(project):
        if project in compiled:
            return
        if not graph[project]:
            compiled.add(project)
            compiled_list.append(project)
            return

        for pr in graph[project]:
            helper(pr)

        compiled_list.append(project)
        compiled.add(project)

    helper(query)
    return f"{len(compiled_list)} {' '.join(compiled_list)}"


if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        input()
        modules = int(input())
        graph = {}
        for _ in range(modules):
            mod, dependencies = input().split(":")
            graph[mod] = dependencies.split()

        queries = int(input())
        compiled = set()
        for _ in range(queries):
            query = input()
            print(compile_project(graph, query, compiled))
        print()
