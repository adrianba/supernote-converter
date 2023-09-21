from fastapi import FastAPI, Request, Response
import supernotelib as sn
import io

app = FastAPI()


@app.post(
    "/pdf",
    response_class=Response,
    responses={200: {"content": {"application/pdf": {}}}},
)
async def convertPdf(request: Request):
    body = await request.body()
    notebook = sn.load(io.BytesIO(body))
    converter = sn.converter.PdfConverter(notebook)
    data = converter.convert(-1, True)
    return Response(content=data, media_type="application/pdf")


@app.post(
    "/txt",
    response_class=Response,
    responses={200: {"content": {"text/plain": {}}}},
)
async def convertText(request: Request):
    body = await request.body()
    notebook = sn.load(io.BytesIO(body))
    converter = sn.converter.TextConverter(notebook)
    total = notebook.get_total_pages()
    data = []
    for i in range(total):
        data.append(converter.convert(i))
    data = list(filter(lambda x: x is not None, data))
    if len(data) > 0:
        data = "\n".join(data)
    return Response(content=data, media_type="text/plain")
