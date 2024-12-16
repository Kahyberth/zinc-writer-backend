

class Zinc:
    def __init__(self, n, m):
        self.n = n 
        self.m = m  
        self.chemicals = []  
        self.raw_materials = []  
        self.demands = {}  

    def read_data(self, data):
        
        self.n = int(data[0].strip())  
        self.m = int(data[1].strip())  

        
        for i in range(self.n):
            line = data[i + 2].split()
            print("Is Line: ", line)
            product_name = " ".join(line[:-self.m - 1])  
            product_values = list(map(int, line[-self.m - 1:]))  
            self.chemicals.append([product_name] + product_values)

        
        for i in range(self.m):
            line = data[i + 2 + self.n].split()
            material_name = " ".join(line[:-2]) 
            material_values = list(map(int, line[-2:])) 
            self.raw_materials.append([material_name] + material_values)

        
        for i in range(2 + self.n + self.m, len(data)):
            line = data[i].split()
            if len(line) >= 3: 
                product_name = " ".join(line[:-2])
                restriction_type = line[-2].lower()
                value = int(line[-1])

                
                if product_name not in self.demands:
                    self.demands[product_name] = {"min": None, "max": None}
                if "minimo" in restriction_type:
                    self.demands[product_name]["min"] = value
                elif "maximo" in restriction_type:
                    self.demands[product_name]["max"] = value

        
        minizinc_code = self.convert_to_code_minizinc()
        return {"message": "Archivo procesado exitosamente", "code": minizinc_code}

    def convert_to_code_minizinc(self):
        minizinc = "% Variables\n"
        
        
        for i in range(self.n):
            minizinc += f"var int: x{i+1};\n"

        
        minizinc += "% No negatividad\n"
        for i in range(self.n):
            minizinc += f"constraint x{i+1} >= 0;\n"

        
        minizinc += "% Restricciones\n"
        for i in range(self.m):
            minizinc += "constraint "
            for j in range(self.n):
                if self.chemicals[j][2 + i] > 0: 
                    minizinc += f"{self.chemicals[j][2 + i]}*x{j+1} + "
            minizinc = minizinc.rstrip("+ ")
            minizinc += f" <= {self.raw_materials[i][2]};\n"

        
        minizinc += "% Restricciones de demanda\n"
        for i, product in enumerate(self.chemicals):
            product_name = product[0]
            if product_name in self.demands:
                if self.demands[product_name]["min"] is not None:
                    minizinc += f"constraint x{i+1} >= {self.demands[product_name]['min']};\n"
                if self.demands[product_name]["max"] is not None:
                    minizinc += f"constraint x{i+1} <= {self.demands[product_name]['max']};\n"

        
        minizinc += "% Función objetivo\nsolve maximize "
        for i in range(self.n):
            profit = self.chemicals[i][1] 
            minizinc += f"{profit}*x{i+1} + "
        minizinc = minizinc.rstrip("+ ")
        minizinc += ";\n"

        return minizinc
