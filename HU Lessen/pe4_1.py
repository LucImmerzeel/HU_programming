cijferICOR = 7.5
cijferPROG = 7.5
cijferCSN = 7.5

gemiddelde = str((cijferCSN + cijferICOR + cijferPROG)/3)
beloning = str(30 * (cijferPROG + cijferICOR + cijferCSN))

overzicht = "Mijn cijfers (gemiddeld een " + gemiddelde + ") leveren een beloning van € " + beloning + " op!"

print(overzicht)