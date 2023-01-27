SQ_SELECT_DOC_ALL = ('select doc.iddocumento'
                          ', doc.nomedoc'
                          ', doc.hash'
                          ', doc.documento'
                          ', gab.idgabarito '
                       'from documento doc '
                       'join gabarito gab '
                         'on gab.iddocumento = doc.iddocumento '
                   'order by doc.iddocumento'
                          ', doc.hash'
                          ', gab.idgabarito')

SQ_SELECT_DOCVAL_ALL = ('select gabv.idgabarito'+
                             ', gabv.idgabaritovalor'+
                             ', gabv.idclasse'+
                             ', gabv.valor'+
                             ', cv.nome '+
                          'from gabaritovalor gabv '+
                          'join classevalor cv '+
                            'on cv.idclasse = gabv.idclasse '+
                      'order by gabv.idgabarito'+
                             ', gabv.idgabaritovalor')
