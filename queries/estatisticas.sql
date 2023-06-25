-- Todos os registros de estatistica
  select * 
    from estatistica e 
order by e.iddocumento;

-- Todos os documentos que não tiveram nenhuma ocorrência de 100%
select distinct d.iddocumento 
              , d.nomedoc 
           from documento d
          where not exists (select 1 
                              from estatistica e
                             where d.iddocumento = e.iddocumento 
                               and e.acerto = 100);

-- Media e total de registros de estatistica 
select avg(e.acerto)
     , count(e.acerto)
  from estatistica e;

-- Média de duração por processamento de documento
select avg(cd.duracao)
  from combinacoesdocumento cd;
 
-- Tempo minímo, médio e máximo de duração por processamento de documento
  select cd.iddocumento
       , min(cd.duracao)
       , avg(cd.duracao)
       , max(cd.duracao)
    from combinacoesdocumento cd
group by cd.iddocumento
order by avg(cd.duracao)
       , cd.iddocumento;
      
  select cast (case  
           when e.acerto between 00 and 09.9999 then '00'
           when e.acerto between 10 and 19.9999 then '10'
           when e.acerto between 20 and 29.9999 then '20'
           when e.acerto between 30 and 39.9999 then '30'
           when e.acerto between 40 and 49.9999 then '40'
           when e.acerto between 50 and 59.9999 then '50'
           when e.acerto between 60 and 69.9999 then '60'
           when e.acerto between 70 and 79.9999 then '70'
           when e.acerto between 80 and 89.9999 then '80'
           when e.acerto between 90 and 99.9999 then '90'
           when e.acerto = 100 then '100'
         end as integer) as intervalo
       , count(*) as quantidade
    from estatistica e
group by intervalo
order by intervalo;

 
-- Média e total por dezenas de registros de estatistica
select (select concat('Média: ', round(avg(e.acerto)::numeric, 0), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto = 100) AS DE_100_A_100
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 90 and 99.9999) AS DE_90_A_99
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 80 and 89.9999) AS DE_80_A_89
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 70 and 79.9999) AS DE_70_A_79
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 60 and 69.9999) AS DE_60_A_69
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 50 and 59.9999) AS DE_50_A_59
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 40 and 49.9999) AS DE_40_A_49
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 30 and 39.9999) AS DE_30_A_39
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 20 and 29.9999) AS DE_20_A_29
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 10 and 19.9999) AS DE_10_A_19
     , (select concat('Média: ', round(avg(e.acerto)::numeric, 4), '%, Contagem: ', count(e.acerto)) from estatistica e where e.acerto between 0 and 9.9999) AS DE_0_A_9
  from combinacoes c 
 where c.idcombinacoes = 1;

select (select count(e.acerto) from estatistica e where e.acerto = 100) AS DE_100_A_100
     , (select count(e.acerto) from estatistica e where e.acerto between 90 and 99.9999) AS DE_90_A_99
     , (select count(e.acerto) from estatistica e where e.acerto between 80 and 89.9999) AS DE_80_A_89
     , (select count(e.acerto) from estatistica e where e.acerto between 70 and 79.9999) AS DE_70_A_79
     , (select count(e.acerto) from estatistica e where e.acerto between 60 and 69.9999) AS DE_60_A_69
     , (select count(e.acerto) from estatistica e where e.acerto between 50 and 59.9999) AS DE_50_A_59
     , (select count(e.acerto) from estatistica e where e.acerto between 40 and 49.9999) AS DE_40_A_49
     , (select count(e.acerto) from estatistica e where e.acerto between 30 and 39.9999) AS DE_30_A_39
     , (select count(e.acerto) from estatistica e where e.acerto between 20 and 29.9999) AS DE_20_A_29
     , (select count(e.acerto) from estatistica e where e.acerto between 10 and 19.9999) AS DE_10_A_19
     , (select count(e.acerto) from estatistica e where e.acerto between 0 and 9.9999) AS DE_0_A_9
  from combinacoes c 
 where c.idcombinacoes = 1;

select e.acerto
     , count(*) as quantidade
 from estatistica e
 group by e.acerto
 order by e.acerto;  
     
-- Combinações que tiveram 100%, ordenados pela maior quantidade de ocorrência 
  select e.idcombinacoes 
       , c.ppldpi 
       , c.ppltransparent 
       , c.pplgrayscale 
       , c.cvequalizehist 
       , c.cvnormalize 
       , c.tssdpi 
       , c.tssoem 
       , c.tsspsm
       , e.acerto
       , count(e.idcombinacoes)
    from estatistica e
    join combinacoes c 
      on c.idcombinacoes = e.idcombinacoes 
   where e.acerto = 100
group by e.idcombinacoes 
       , c.ppldpi 
       , c.ppltransparent 
       , c.pplgrayscale 
       , c.cvequalizehist 
       , c.cvnormalize 
       , c.tssdpi 
       , c.tssoem 
       , c.tsspsm
       , e.acerto
order by count(e.idcombinacoes) desc
       , e.idcombinacoes;
      
  select e.idcombinacoes 
       , e.acerto
       , count(e.idcombinacoes)
    from estatistica e
    join combinacoes c 
      on c.idcombinacoes = e.idcombinacoes
   --where e.acerto = 100
group by e.idcombinacoes 
       , e.acerto
order by e.acerto desc
       , count(e.idcombinacoes) desc
       , e.idcombinacoes;
      
  select e.acerto
       , count(e.idcombinacoes)
    from estatistica e
    join combinacoes c 
      on c.idcombinacoes = e.idcombinacoes
group by e.acerto
order by e.acerto;
  
  select e.idcombinacoes 
       , e.acerto
    from estatistica e
    join combinacoes c 
      on c.idcombinacoes = e.idcombinacoes 
order by e.acerto desc
       , e.idcombinacoes;
      
-- Total de documentos
select count(*) 
  from documento d; 

-- Total de valores extraídos dos documentos
select count(*)
  from documentovalor dv;

-- Todos os registros de valores extraídos dos documentos
   select dv.iddocumento 
        , dv.iddocumentovalor 
        , dv.idcombinacoes 
        , dv.idclasse 
        , cv.nome
        , dv.valor 
     from documentovalor dv
     join classevalor cv
       on cv.idclasse = dv.idclasse      
 order by dv.iddocumento
        , dv.iddocumentovalor
        , dv.idcombinacoes
        , dv.idclasse;
       
-- Todos os registros de valores extraídos dos documentos
   select dv.iddocumento 
        , dv.iddocumentovalor 
        , dv.idcombinacoes 
        , dv.idclasse 
        , cv.nome
        , dv.valor 
     from documentovalor dv
     join classevalor cv
       on cv.idclasse = dv.idclasse
 order by dv.iddocumento
        , dv.iddocumentovalor
        , dv.idcombinacoes
        , dv.idclasse;
 
-- Total de combinações
select count(*)
  from combinacoes c;
