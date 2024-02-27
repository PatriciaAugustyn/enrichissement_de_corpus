def read_annotations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

def calculate_metrics(automatic_annotations, manual_annotations):
    true_positives = len(automatic_annotations.intersection(manual_annotations))
    false_positives = len(automatic_annotations - manual_annotations)
    false_negatives = len(manual_annotations - automatic_annotations)

    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives != 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives != 0 else 0

    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 0

    return precision, recall, f1_score

# Exemple d'utilisation
automatic_file_path = 'resultat_stanza_hanouna.txt'
manual_file_path = 'stanza_annotation_manuel.txt'

automatic_annotations = read_annotations(automatic_file_path)
manual_annotations = read_annotations(manual_file_path)

precision, recall, f1_score = calculate_metrics(automatic_annotations, manual_annotations)

print(f'Précision: {precision:.4f}')
print(f'Rappel: {recall:.4f}')
print(f'F-mesure: {f1_score:.4f}')
