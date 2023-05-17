SE_SEQ_BASE = ("do $$ "
               "begin "
                 "if not exists (select 1 from information_schema.sequences where sequence_name = '{0}') then "
                   "create sequence {0} start 1; "
                 "end if; "
               "end $$;")

SE_SEQCLASSEVALOR = SE_SEQ_BASE.format('seqclassevalor')
SE_DROPSEQCLASSEVALOR = 'drop sequence if exists seqclassevalor'

SE_SEQDOCUMENTO = SE_SEQ_BASE.format('seqdocumento')
SE_DROPSEQDOCUMENTO = 'drop sequence if exists seqdocumento'

SE_SEQGABARITO = SE_SEQ_BASE.format('seqgabarito')
SE_DROPSEQGABARITO = 'drop sequence if exists seqgabarito'