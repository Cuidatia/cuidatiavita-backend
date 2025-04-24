from flask import jsonify

from models.entities.Organizacion import Organizacion

class ModelOrganizacion():
    @classmethod
    def getOrganizacion(cls, mysql, id):
        
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM organizaciones WHERE id = %s", (id))
            row = cursor.fetchone()
            
            organizacion = Organizacion(row[0], row[1])
                    
            return organizacion.to_dict()
        
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            conn.close()