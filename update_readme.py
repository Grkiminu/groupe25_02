
import os
from datetime import datetime

# Configuration
PROJECT_NAME = "groupe25_02"
USER_INFO = {
    "NOM": "KIMINU",
    "POST NOM": "TEMBO",
    "PRENOM": "GRADI",
    "PROMO": "L2",
    "DEPARTEMENT": "GEI(Genie Electrique et Informatique)"
}
THIS_PATH = "update_readme.py"
README_PATH = "README.md"
IGNORE_DIRS = [".git", "pycache", "venv", ".github", ".idea"]
IGNORE_FILES = [README_PATH, ".DS_Store", "*.pyc", THIS_PATH]


def generate_tree(start_path="."):
    """Génère une arborescence parfaitement alignée"""
    base_name = os.path.basename(os.path.abspath(start_path))
    tree_lines = [f"📦 {base_name}"]

    for root, dirs, files in os.walk(start_path):
        # Nettoyage des éléments à ignorer
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        files = [f for f in files if not any(f.endswith(ext) for ext in IGNORE_FILES)]

        level = root.replace(start_path, "").count(os.sep)

        if level == 0:
            continue

        # Calcul de l'indentation
        is_last_dir = (dirs == [] and files == [])
        indent = "    " * (level - 1)
        branch = "└── " if is_last_dir else "├── "

        tree_lines.append(f"{indent}{branch}📂 {os.path.basename(root)}")

        # Gestion des fichiers
        sub_indent = "    " * level

        for i, f in enumerate(files):
            is_last_file = (i == len(files) - 1)
            file_branch = "└── " if is_last_file else "├── "
            tree_lines.append(f"{sub_indent}{file_branch}📄 {f}")

    return "\n".join(tree_lines)


def create_readme():
    """Crée un README parfaitement formaté"""
    with open(README_PATH, "w", encoding="utf-8") as f:
        # En-tête
        f.write(f"# {PROJECT_NAME}<br>\n")

        # Sections texte
        sections = [
            ("## BREVE DESCRIPTION", "Dossier github pour les TP et TD d'algo et Programmation L2 POLYTECHNIQUE UNIKIN.<br>Ce fichier \"README.md\" est généré automatiquement par un script python que j'ai créé \"update_readme.py\" qui se trouve a la racine de mon repertoire"),
            ("## INFORMATIONS PERSONELLES",
             "<br>\n".join(f"{k}: {v}" for k, v in USER_INFO.items())),
            ("## ARBORESCENCE", f"`ARBRE<br><pre>\n{generate_tree()}<br>\n```")
        ]

        for title, content in sections:
            f.write(f"{title}<br>\n{content}<br>\n")

        # Pied de page
        f.write(f"> Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    create_readme()
    print(f"README généré avec succès dans {README_PATH}")
