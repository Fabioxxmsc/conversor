SC_INSERTCLASSEVALOR = 'insert into classevalor (idclasse, nome) values (%s, %s)'

SC_INSERTDOCUMENTO = 'insert into documento (iddocumento, nomedoc, hash, documento) values (%s, %s, %s, %s)'

SC_INSERTDOCUMENTOVALOR = 'insert into documentovalor (iddocumento, iddocumentovalor, idclasse, valor) values (%s, %s, %s, %s)'

SC_INSERTGABARITO = 'insert into gabarito (idgabarito, iddocumento) values (%s, %s)'

SC_INSERTGABARITOVALOR = 'insert into gabaritovalor (idgabarito, idgabaritovalor, idclasse, valor) values (%s, %s, %s, %s)'