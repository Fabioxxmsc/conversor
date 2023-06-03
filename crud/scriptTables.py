ST_CLASSEVALOR = ('create table if not exists classevalor ('
                  'idclasse int4 not null'
                  ', nome varchar(255) not null'
                  ', constraint unclassevalornome unique (nome)'
                  ', constraint pkclassevalor primary key (idclasse)'
                  ')')

ST_DROPCLASSEVALOR = 'drop table if exists classevalor'

#----------------------------------------------------------------
ST_DOCUMENTO = ('create table if not exists documento ('
                'iddocumento int4 not null'
                ', nomedoc varchar(255) not null'
                ', hash varchar(255) not null'
                ', documento bytea not null'
                ', constraint pkdocumento primary key (iddocumento)'
                ')')

ST_DROPDOCUMENTO = 'drop table if exists documento'

#----------------------------------------------------------------
ST_DOCUMENTOVALOR = ('create table if not exists documentovalor ('
                     'iddocumento int4 not null'
                     ', iddocumentovalor int4 not null'
                     ', idcombinacoes int4 not null'
                     ', idclasse int4 not null'
                     ', valor bytea'
                     ', constraint pkdocumentovalor primary key (iddocumento, iddocumentovalor)'
                     ', constraint fkdocumentovalorcla foreign key (idclasse) references classevalor (idclasse)'
                     ', constraint fkdocumentovalordoc foreign key (iddocumento) references documento (iddocumento)'
                     ', constraint fkdocumentovalorcomb foreign key (idcombinacoes) references combinacoes (idcombinacoes)'
                     ')')

ST_DROPDOCUMENTOVALOR = 'drop table if exists documentovalor'

#----------------------------------------------------------------
ST_GABARITO = ('create table if not exists gabarito ('
               'idgabarito int4 not null'
               ', iddocumento int4 not null'
               ', constraint pkgabarito primary key (idgabarito)'
               ', constraint fkgabaritodocumento foreign key (iddocumento) references documento (iddocumento)'
               ')')

ST_DROPGABARITO = 'drop table if exists gabarito'

#----------------------------------------------------------------
ST_GABARITOVALOR = ('create table if not exists gabaritovalor ('
                    'idgabarito int4 not null'
                    ', idgabaritovalor int4 not null'
                    ', idclasse int4 not null'
                    ', valor varchar(255)'
                    ', constraint pkgabaritovalorg primary key (idgabarito, idgabaritovalor)'
                    ', constraint fkgabaritovalorcla foreign key (idclasse) references classevalor (idclasse)'
                    ', constraint fkgabaritovalorgab foreign key (idgabarito) references gabarito (idgabarito)'
                    ')')

ST_DROPGABARITOVALOR = 'drop table if exists gabaritovalor'

#----------------------------------------------------------------
ST_COMBINACOES = ('create table if not exists combinacoes ('
                  'idcombinacoes int4 not null'
                  ', pplDpi varchar(5)'
                  ', pplTransparent varchar(5)'
                  ', pplGrayscale varchar(5)'
                  ', cvEqualizeHist varchar(5)'
                  ', cvNormalize varchar(5)'
                  ', tssDpi varchar(5)'
                  ', tssOem varchar(5)'
                  ', tssPsm varchar(5)'
                  ', constraint pkcombinacoes primary key (idcombinacoes)'
                  ')')

ST_DROPCOMBINACOES = 'drop table if exists combinacoes'

#----------------------------------------------------------------
ST_COMBINACOESDOCUMENTO = ('create table if not exists combinacoesdocumento ('
                           'iddocumento int4 not null'
                           ', idcombinacoes int4 not null'
                           ', status smallint not null'
                           ', duracao interval not null'
                           ', constraint pkcombinacoesdocumento primary key (iddocumento, idcombinacoes)'
                           ', constraint fkcombinacoesdocumentodoc foreign key (iddocumento) references documento (iddocumento)'
                           ', constraint fkcombinacoesdocumentocom foreign key (idcombinacoes) references combinacoes (idcombinacoes)'
                           ')')

ST_DROPCOMBINACOESDOCUMENTO = 'drop table if exists combinacoesdocumento'

#----------------------------------------------------------------
ST_ESTATISTICA = ('create table if not exists estatistica ('
                  'iddocumento int4 not null'
                  ', idgabarito int4 not null'
                  ', idgabaritovalor int4 not null'
                  ', idcombinacoes int4 not null'
                  ', acerto numeric(6, 4) not null'
                  ', constraint pkestatistica primary key (iddocumento, idgabarito, idgabaritovalor, idcombinacoes)'
                  ', constraint fkestatisticadocumento foreign key (iddocumento) references documento (iddocumento)'
                  ', constraint fkestatisticagabarito foreign key (idgabarito) references gabarito (idgabarito)'
                  ', constraint fkestatisticagabaritovalor foreign key (idgabarito, idgabaritovalor) references gabaritovalor (idgabarito, idgabaritovalor)'
                  ', constraint fkestatisticacombinacoes foreign key (idcombinacoes) references combinacoes (idcombinacoes)'
                  ')')

ST_DROPESTATISTICA = 'drop table if exists estatistica'