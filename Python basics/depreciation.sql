--Depreciation 

/*Table for entered info*/
select * from r5objdeptypes

/*Table for calculations*/
 select * from  R5OBJDEPRECIATION
 


/* base for query */
select obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes'
  from R5OBJDEPTYPES



  /*if value change */
select obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes'
  from R5OBJDEPTYPES
  where OBD_CHANGEVALUE is not null 



 /*if life change*/
   select obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes'
  from R5OBJDEPTYPES
  where OBD_CHANGELIFE is not null
  
  
   
/*if Book value is less than set number */
SELECT * FROM (
    SELECT 
      odp_object, Date = cast(odp_startdate AS DATE),  
	  convert(decimal(20, 2), ODP_BOOKVALUE)  as 'Book Value' ,
	  obj_status as 'Status',  
	  Past_Due = DATEDIFF(day, odp_startdate, GetDate()),  
	  RN = ROW_NUMBER()OVER(PARTITION BY odp_object ORDER BY odp_bookvalue desc)
    FROM R5OBJDEPRECIATION 
	join r5objects on obj_code = ODP_OBJECT 
	where (odp_bookvalue < 15000) and (ODP_STARTDATE < GETDATE()) 
) R5OBJDEPRECIATION
WHERE RN = 1





 /* if life is less than 2 years */
Select * From (
 select 
RN = ROW_NUMBER()OVER(PARTITION BY obd_object ORDER BY obd_estlife desc),
obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes'
  from R5OBJDEPTYPES
  where OBD_ESTLIFE < 2)
  R5OBJDEPTYPES
WHERE RN = 1




  /* if selling value is greater than book value broke only returning top hit of entire db not top1 of each hit*/
select TOP 1 obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes',
convert(DOUBLE PRECISION, round(ODP_BOOKVALUE, 2)) as 'Book Value'
  from R5OBJDEPTYPES
  inner join R5OBJDEPRECIATION on ODP_OBJECT = OBD_OBJECT
  where OBD_RESIDUAL > 0 
   and ODP_BOOKVALUE <=  obd_residual





/*Returns # of counts example this returns book value under an arbitrary # and days it has been  */

SELECT Count(*) FROM (
    SELECT   
	  RN = ROW_NUMBER()OVER(PARTITION BY odp_object ORDER BY odp_bookvalue desc)
    FROM R5OBJDEPRECIATION 
	where (odp_bookvalue < 15000) and (ODP_STARTDATE < GETDATE()) 
) R5OBJDEPRECIATION
WHERE RN = 1

select * from R5OBJDEPRECIATION

/*---------tests below-----------------------------------*/

 /* playground for building db query*/
select obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes',
convert(DOUBLE PRECISION, round(ODP_BOOKVALUE, 2)) as 'Book Value',
cast(ODP_ENDDATE as date) as 'Book Date'
  from R5OBJDEPTYPES
   join R5OBJDEPRECIATION on ODP_OBJECT = OBD_OBJECT
  where 
 ODP_BOOKVALUE >= (obd_residual + 5000) and obd_depcategory <> 'C' 


SELECT * FROM (
    SELECT 
      odp_object, Date = cast(odp_startdate AS DATE),  convert(DOUBLE PRECISION, odp_bookvalue) AS 'VALUE' , Past_Due = DATEDIFF(day, odp_startdate, GetDate()),  RN = ROW_NUMBER()OVER(PARTITION BY odp_object ORDER BY odp_bookvalue desc),
    obj_status as 'STATUS'
    FROM R5OBJDEPRECIATION 
	join r5objects on obj_code = ODP_OBJECT 
	where (odp_bookvalue < 15000) and (ODP_STARTDATE < GETDATE()) 
) R5OBJDEPRECIATION
WHERE RN = 1

Select * From (
 select 
RN = ROW_NUMBER()OVER(PARTITION BY obd_object ORDER BY obd_estlife desc),
obd_object as 'Equipment', 
cast(obd_startdate AS DATE) as 'Event Date', 
convert(DOUBLE PRECISION, OBD_ORIGVALUE)  as 'Orig. Value',
convert(DOUBLE PRECISION, obd_residual) as 'Exp. Selling Cost',
obd_depcategory as 'Change In Cal.',
convert(DOUBLE PRECISION,obd_changevalue) as 'Change Value',  
convert(DOUBLE PRECISION, obd_changelife) as 'Life Change',
obd_estlife as 'Exp. Life Rem.', 
OBD_NOTES as 'Notes'
  from R5OBJDEPTYPES
  where OBD_ESTLIFE < 2)
  R5OBJDEPTYPES
WHERE RN = 1

select* from R5OBJECTS
where OBJ_USER like '%HEPHNERA%'

SELECT TOP 10 * FROM R5OBJDEPRECIATION 