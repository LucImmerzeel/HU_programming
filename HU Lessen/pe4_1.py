cijferICOR = 7.5
cijferPROG = 7.5
cijferCSN = 7.5

gemiddelde = (cijferCSN+cijferICOR+cijferPROG)/3
beloning = str(30 * (cijferPROG + cijferICOR + cijferCSN))

print("Mijn cijfers (gemiddeld een ", end='')
print(gemiddelde, end='')
print(") leveren een beloning van € ", end='')
print(beloning , end = "")
print(" op!")