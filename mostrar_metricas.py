
def mostrar_metricas(rmse, cnr, ambe):
    print("Erro quadrático médio")
    print(f"RMSE: Equalização do Histograma: {rmse[1]};\nRMSE: Filtro Bilateral: {rmse[0]};")
    print(f"RMSE: Correção de gama = 1.5: {rmse[2]};\nRMSE: Correção de gama = 0.6 {rmse[3]}.")
    print(f"RMSE:  Equa. de Hist. p/ Correção de gama = 3.5: {rmse[4]}.\n************************************")

    print("Erro de brilho médio absoluto")
    print(f"AMBE: Equalização do Histograma: {ambe[1]};\nAMBE: Filtro Bilateral: {ambe[0]}.")
    print(f"AMBE: Correção de gama = 1.5: {ambe[2]};\nAMBE: Correção de gama = 0.6 {ambe[3]}.")
    print(f"AMBE:  Equa. de Hist. p/ Correção de gama = 3.5: {ambe[4]}.\n************************************")

    print("Relação de contraste para ruído")
    print(f"CNR: Equalização do Histograma: {cnr[1]};\nCNR: Filtro Bilateral: {cnr[0]};")
    print(f"CNR: Correção de gama = 1.5: {cnr[2]};\nCNR: Correção de gama = 0.6 {cnr[3]};")
    print(f"CNR:  Equa. de Hist. p/ Correção de gama = 3.5: {cnr[4]}.\n************************************")

