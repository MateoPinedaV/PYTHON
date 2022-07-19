cuenta_archivos = {"jpg":10,"txt":14,"csv":2,"py":23}
for extension in cuenta_archivos:
    print(extension)

for ext, amount in cuenta_archivos.items():
    print("Aqui hay {} Archivos con la .{} extension".format(amount,ext))