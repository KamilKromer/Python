n = int(input())

for _ in range(n):
    alp = input()
    alpL = []
    for s in alp:
        alpL.append(s)

    # Dane są gotowe w liście
    sum = -1

    for ind_ in range(len(alpL)):
        cur = alpL[ind_]

        if not "Z" in alpL and sum == -1: # Specyficzny przypadek kiedy wszyscy mają line
            sum = 0
            break

        if cur == "B" and "Z" in alpL: # Jeżeli Z nie znajduje się w liście to jest to koniec

            omit_indexes = []
            for ind2_ in range(ind_, len(alpL) - 1): # Musimy zrobić rekursję żeby skalkulować kroki które dzieją się równolegle

                cur2 = alpL[ind2_]

                if cur2 == 'B' and not ind2_ in omit_indexes: # Musimy sprawdzić czy właśnie nie przekształciliśmy tej litery
                    if alpL[ind2_ + 1] == 'Z':
                        omit_indexes.append(ind2_+1)
                        alpL[ind2_ + 1] = "B" # Przekaż line i zapisz
            
            if sum == -1:
                sum = 1
            else:
                sum += 1

        else: break
    
    print(sum)
    
