d1= {
    "producto": "TV 55´",
    "precio": 120,
    "cantidad": 2,
}

dscto_1= 10

costo_total= (d1["precio"])*(d1["cantidad"])

if costo_total> 100:
    costo_total *= 0.9
    print("El costo total a pagar es de: {}".format(costo_total))

else:
    print("No tiene descuento por aplicar")






