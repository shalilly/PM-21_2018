

gueltige_nukleotide = ['A', 'T', 'G', 'C']
l_g = []
l_a = []
l_t = []
l_c = []

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.
    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """

    # mithilfe von while-Schleife die Sequenz abfragen 
    
    x = 0
    
    while True:
        global sequence
        sequence = input('Gib eine DNA-Sequenz ein: ')
       
        # Überprüfen, ob alle eingegebenen Buchstaben Basen sind. 
        # Wenn ja, müssen die Basen gezählt bzw. erst mal sortiert werden 
        #  -> Listen 
        # Wenn nicht: Fehlermeldung ausgeben und loop abbrechen 
        
        try:
            while True: 
                sequence[x] in gueltige_nukleotide 
            
                if sequence[x] == gueltige_nukleotide[3]:
                    l_g.append('G')
                elif sequence[x] == gueltige_nukleotide[0]:
                    l_a.append('A')
                elif sequence[x] == gueltige_nukleotide[1]:
                    l_t.append('T')
                elif sequence[x] == gueltige_nukleotide[2]:
                    l_c.append ('C')
                else: 
                    sequence[x] + 2
            # hier inneren loop abbrechen und äußeren wiederholen.
            # aber nur bei dieser else Bedingung
            # nicht, wenn der while-loop aus anderen Gründen abgebrochen wird
            # nur wieeeeeeee ???????????????????????????? ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
            
                x = x + 1 
                if x == len(sequence):
                    break
                else: 
                    continue
                    
                
        except TypeError:             
            print()
            print('Bei der Eingabe handelt es sich ' 
                  'nicht um eine gültige DNA-Sequenz!')
            print()
            print()
            continue
       
        return sequence

# Jetzt kommt die Ausführung der Definition 

seq = hole_dna_sequenz()

# Dann werden zusätzliche Werte berechnet und/oder ausgegeben

print()
print('Eingelesene Sequenz:') 
print()
print(sequence)
print()
print('Länge:' , len(sequence))
print()
print('Base    Häufigkeit') 
print('G               ' , len(l_g))
print('A               ' , len(l_a))
print('T               ' , len(l_t))
print('C               ' , len(l_c))
print()
print('% CG-Gehalt:' , 
      ((len(l_g)+len(l_c))*100)/(len(l_g)+len(l_c)+len(l_t)+len(l_a)))
print()
print('Molekulargewicht:' , 
      (mw_g*len(l_g)+mw_a*len(l_a)+mw_t*len(l_t)+mw_c*len(l_c)+mw_oh)/1000 , 
      'g/mol')
