import flet as ft
from lib2to3.tests.data import false_encoding

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es: {imc:.2f}"
        page.update()
        
        #Funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        
        #Validar condiciones del IMC
        if imc<18.5:
            dialog=ft.AlertDialog(
                title = ft.Text("resultado de IMC"),
                content=ft.Text("Alctualmente estas bajo peso "),
                actions=[ft.TextButton("OK",on_clck=cerrar_dialogo)],
            )
        elif imc >=18.5 and imc <24.9:
            dialog = ft.AlertDialog(
                title=ft.Text("resultado de IMc"),
                content=ft.Text("Tu peso es normal")
                actions=[ft.TextButton("ok",on_click=cerrar dialogo)]
            )
        elif imc >= 25 and imc < 30:
            dialog=ft.AlertDialog(
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("tienes sobrepeso"),
                actions=[ft.TextButton("OK",on_click=cerrar_dialogo)]
            )
        else:
            dialog= ft.AlertDialog(
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("tienes obecidad"),
                actions=[ft.TextButton("ok",on_click=cerrar_dialogo)]
            )
    except ValueError:
        def cerrar_dialogo(e):
            page.dialog.open=False
            page.update()
            
            dialog=ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("debes ibngresar valores numericos")
                actions=[ft.TextButton("ok",on_click=cerrar_dialogo)]
            )


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="purple"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMc es:")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    
    def on_calcular(e):
        calcular_imc(txtPeso, txtAltura, lblIMC, page)
    
    def on_limpiar(e):
        txtPeso.value=""
        txtAltura=""
        lblIMC="tu IMC es: "
        page.update()
    
    btnCalcular=ft.ElevatedButton("Calcular",on_click)
    btnLimpiar=ft.ElevatedButton("limpiar", on_click)
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,
                txtAltura,
                lblIMC
                ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,
                btnLimpiar
            ],alignment="CENTER"
        )
        )

ft.app(target = main)
