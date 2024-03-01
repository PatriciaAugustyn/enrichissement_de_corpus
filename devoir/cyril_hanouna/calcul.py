def read_annotations(path):
    with open(path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

def calcul_automatic(automatic_annotations, manual_annotations):
    true_positives = len(automatic_annotations.intersection(manual_annotations))
    false_positives = len(automatic_annotations - manual_annotations)
    false_negatives = len(manual_annotations - automatic_annotations)

    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives != 0 else 0
    rappel = true_positives / (true_positives + false_negatives) if true_positives + false_negatives != 0 else 0

    f_score = 2 * (precision * rappel) / (precision + rappel) if precision + rappel != 0 else 0

    return precision, rappel, f1_score

# Exemple d'utilisation
automatic_file = 'nom_fichier_resultat.txt'
manual_file = 'nom_fichier_annotation-manuel.txt'

automatic_annotations = read_annotations(automatic_file)
manual_annotations = read_annotations(manual_file)

precision, rappel, f_score = calcul_automatic(automatic_annotations, manual_annotations)

print(f'Précision: {precision:.4f}')
print(f'Rappel: {rappel:.4f}')
print(f'F-mesure: {f_score:.4f}')
