import stanza

nlp_pos = stanza.Pipeline('fr',processors='tokenize,lemma,pos,ner')
filename = "bonheur.txt"
with open(filename, 'r') as fichier:
    doc = fichier.read()
def process_text(fichier):
    # Traiter le texte avec Stanza
    doc = nlp_pos(fichier)
    
    # Afficher les résultats
    for sentence in doc.sentences:
        for word in sentence.words:
              print(f"Mot : {word.text}\tLemme : {word.lemma}\tPOS : {word.pos}\t")

process_text(doc)


