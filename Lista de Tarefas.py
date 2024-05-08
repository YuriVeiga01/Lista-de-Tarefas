class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
            self.tasks.append(task)
            print(f"Tarefa ´{task}´adicionada com sucesso!")

    def remove_task(self,task):
                if task in self.tasks:
                    self.tasks.remove(task)
                    print (f"Tarefa ´{task}´ removida com sucesso!")
                else:
                    print(f"Tarefa ´{task}´não encontrada na lista.")
    def show_tasks(self):
        if self.tasks:
            print("Lista de Tarefas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Lista de Tarefas vazia.")
    def main():
        todo_list = TodoList()

        while True:
            print("/n1. Adicionar Tarefa")
            print("2. Remover Tarefa")
            print("3. Mostrar Tarefas")
            print("4. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                task = input("Digite a tarefa a ser adicionada: ")
                todo_list.add_task(task)
            elif choice == "2":
                task = input ("Digite a tarefa a ser removida: ")
                todo_list.remove_task(task)
            elif choice == "3":
                todo_list.show_tasks()
            elif choice == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente. ")

if __name__ == "__main__":
    main()







