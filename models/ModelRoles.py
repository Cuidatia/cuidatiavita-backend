from flask import jsonify
from models.entities.Roles import Roles

class ModelRoles():
    
    @classmethod
    def getAllRoles(cls,mysql):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM roles WHERE id != 1 AND id != 7")
            
            rows = cursor.fetchall()
            rolesList= []
            
            for row in rows:
                roles = Roles(row[0],row[1],row[2])
                rolesList.append(roles.to_dict())
                
            return rolesList
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()