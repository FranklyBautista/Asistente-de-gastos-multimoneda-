begin;
select plan(1);
select has_schema('public', 'el esquema public existe');
select * from finish();
rollback;
