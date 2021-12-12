from fastapi import APIRouter
from sqlalchemy.sql.elements import Cast, between
from sqlalchemy.sql.expression import bindparam, null, select
from sqlalchemy.orm import aliased
from sqlalchemy.sql.sqltypes import String
from model.turn_state import turn_states
from model.turn import turns
from model.user import users
from config.db import conn
from io import BytesIO
from starlette.responses import StreamingResponse
import xlsxwriter
reporte = APIRouter()
@reporte.get("/reporte", response_description='xlsx')
async def payments():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = conn.execute(document_types.select()).fetchall()
    print(data)
    bold = workbook.add_format({'bold': True})
    i = 0
    for key in data[0].keys():
        print(key)
        worksheet.write(0, i, key,bold)
        i=i+1
    m = 1
    for item in data:
        j=0
        for value in item.values():
            worksheet.write(m, j, value)
            j=j+1
        m=m+1

    workbook.close()
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="filenmae3.xlsx"'
    }
    return StreamingResponse(output, headers=headers)
@reporte.get("/reporte_servicio/{fecha_ini}/{fecha_fin}", response_description='xlsx')
async def payments(fecha_ini:str,fecha_fin:str):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    user_client = aliased(users)
    user_mechanical = aliased(users)
    query= select(turns.c.id,
            Cast(turns.c.date,String),
            Cast(turns.c.hora,String),
            (user_mechanical.c.name).label('name_mechanical'),
            (user_mechanical.c.number_document).label('document_mechanical'),
            (user_client.c.name).label('name_client'),
            (user_client.c.number_document).label('document_client'),
            turns.c.observation,
            turns.c.number_plate,
            (turn_states.c.name).label('turn_state'),
            ).select_from(
            turns.join(user_mechanical,turns.c.fk_id_mechanical_user == user_mechanical.c.id)
            .join(user_client,turns.c.fk_id_client_user == user_client.c.id)
            .join(turn_states,turns.c.fk_id_turn_state == turn_states.c.id)
        ).where(between( turns.c.date,fecha_ini,fecha_fin))
    data = conn.execute(query).fetchall()
    # print(data)
    bold = workbook.add_format({'bold': True})
    i = 0
    for key in data[0].keys():
        print(key)
        worksheet.write(0, i, key,bold)
        i=i+1
    m = 1
    for item in data:
        j=0
        for value in item.values():
            worksheet.write(m, j, value)
            j=j+1
        m=m+1

    workbook.close()
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="filenmae3.xlsx"'
    }
    return StreamingResponse(output, headers=headers)