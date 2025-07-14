import subprocess
import graphviz


def generar_archivo_dot():
    # genera archivo .dot
    subprocess.run(
        ['git', 'graph', '-c', '-p', './demo']
    )

    # carga el archivo .dot y lo convierte a imagen
    with open('demo/git_graph.dot') as f:
        dot_graph = f.read()
        graph = graphviz.Source(dot_graph, format='png')
        graph.render('demo/git_graph.png', cleanup=True)  # guarda imagen y limpia archivos temporales
        graphviz.Source.from_file('demo/git_graph.dot')


if __name__ == "__main__":
    generar_archivo_dot()
