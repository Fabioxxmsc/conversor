SELECT_CASE_COUNT_ESTATISTICA = ("select cast (case "
                                                 "when e.acerto between 00 and 09.9999 then '00' "
                                                 "when e.acerto between 10 and 19.9999 then '10' "
                                                 "when e.acerto between 20 and 29.9999 then '20' "
                                                 "when e.acerto between 30 and 39.9999 then '30' "
                                                 "when e.acerto between 40 and 49.9999 then '40' "
                                                 "when e.acerto between 50 and 59.9999 then '50' "
                                                 "when e.acerto between 60 and 69.9999 then '60' "
                                                 "when e.acerto between 70 and 79.9999 then '70' "
                                                 "when e.acerto between 80 and 89.9999 then '80' "
                                                 "when e.acerto between 90 and 99.9999 then '90' "
                                                 "when e.acerto = 100 then '100' "
                                               "end as integer) as intervalo"
                                      ", count(*) as quantidade "
                                   "from estatistica e "
                               "group by intervalo "
                               "order by intervalo")

SELECT_ACERTO_QTD_EST = 'select e.acerto, count(*) as quantidade from estatistica e group by e.acerto order by e.acerto'