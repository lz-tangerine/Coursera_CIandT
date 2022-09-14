def read_db_table(centro_custo):
    spark.sql(f"""SELECT CENTRO_CUSTO.CAG,
                         CENTRO_CUSTO.CCTA,
                         CMCT.CCPF_CNPJ,
                         CMCT.RCLI,
                         CENTRO_CUSTO.CPRODT,
                         CENTRO_CUSTO.COPER,
                         CENTRO_CUSTO.VOPER,
                         CENTRO_CUSTO.ICANAL,
                         CENTRO_CUSTO.DOPER,
                         CENTRO_CUSTO.CSIST                 
                     FROM {centro_custo} as CENTRO_CUSTO
                         LEFT JOIN exp_alta_renda.tmp_cmct_cadu AS CMCT
                                   ON CMCT.CAG = CENTRO_CUSTO.CAG
                                   AND CMCT.CCTA = CENTRO_CUSTO.CCTA
                     GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                     ORDER BY DOPER""").show()


centro_custo = 'exp_alta_renda.tmp_jcot'

read_db_table(centro_custo)