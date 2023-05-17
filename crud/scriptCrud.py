SC_INSERTCLASSEVALOR = 'insert into classevalor (idclasse, nome) values (%s, %s) on conflict do nothing'

SC_INSERTDOCUMENTO = 'insert into documento (iddocumento, nomedoc, hash, documento) values (%s, %s, %s, %s)'

SC_INSERTDOCUMENTOVALOR = 'insert into documentovalor (iddocumento, iddocumentovalor, idclasse, valor) values (%s, %s, %s, %s)'
SC_DELETEDOCUMENTOVALOR = 'delete from documentovalor dv where dv.iddocumento = %s and dv.iddocumentovalor = %s'

SC_INSERTGABARITO = 'insert into gabarito (idgabarito, iddocumento) values (%s, %s)'

SC_INSERTGABARITOVALOR = 'insert into gabaritovalor (idgabarito, idgabaritovalor, idclasse, valor) values (%s, %s, %s, %s)'

SC_INSERTCOMBINACOES = ('insert into combinacoes (idcombinacoes, pplDpi, pplTransparent, pplGrayscale, cvEqualizeHist, cvNormalize, tssDpi, tssOem, tssPsm) '+
                        'values (%s, %s, %s, %s, %s, %s, %s, %s, %s) on conflict do nothing')

SC_INSERTCOMBINACOESDOCUMENTO = 'insert into combinacoesdocumento (iddocumento, idcombinacoes, status) values (%s, %s, %s)'
SC_DELETECOMBINACOESDOCUMENTO = 'delete from combinacoesdocumento cd where cd.iddocumento = %s and cd.idcombinacoes = %s'