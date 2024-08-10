#precio neto
# es el precio sin iva, es quien regleja los impuestos  

#encontrar el precio neto

def precioNeto(iva,precio_bruto):
    resultado = precio_bruto / iva
    impuesto_valor = resultado * 0.12
    return resultado , impuesto_valor


#botella de agua 
precio_bruto = 5 
IVA = 1.12
precio_neto = precioNeto(IVA,precio_bruto)

#ejemplo te frio  de 340ml
producto = "te_frio" 
precio_bruto = 12
IVA = 1.12
impuesto_valor = 0.12
precio_neto = precioNeto(IVA,precio_bruto)
print(f"producto:{producto} producto_bruto:Q{precio_bruto} precio neto:Q{precio_neto}impuesto_valor:Q{impuesto_valor}")