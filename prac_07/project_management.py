import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display completed and incomplete projects sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(complete_projects):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Filter projects by start date."""
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    new_completion = input("New completion percentage (leave blank to keep current): ")
    if new_completion:
        project.completion_percentage = int(new_completion)

    new_priority = input("New priority (leave blank to keep current): ")
    if new_priority:
        project.priority = int(new_priority)


def main():
    """Main program function."""
    filename = "projects.txt"
    projects = load_projects(filename)

    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print("Welcome to Pythonic Project Management")

    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yyyy): "), "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to the default file? (y/n): ").lower()
            if save_choice == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
