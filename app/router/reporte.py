from fastapi import APIRouter
from model.document_type import document_types
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