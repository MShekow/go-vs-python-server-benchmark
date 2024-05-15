package migrations

import (
	"encoding/json"

	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	m "github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models"
)

func init() {
	m.Register(func(db dbx.Builder) error {
		jsonData := `[
			{
				"id": "_pb_users_auth_",
				"created": "2024-05-15 06:52:52.072Z",
				"updated": "2024-05-15 06:52:52.074Z",
				"name": "users",
				"type": "auth",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "users_name",
						"name": "name",
						"type": "text",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "users_avatar",
						"name": "avatar",
						"type": "file",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"mimeTypes": [
								"image/jpeg",
								"image/png",
								"image/svg+xml",
								"image/gif",
								"image/webp"
							],
							"thumbs": null,
							"maxSelect": 1,
							"maxSize": 5242880,
							"protected": false
						}
					}
				],
				"indexes": [],
				"listRule": "id = @request.auth.id",
				"viewRule": "id = @request.auth.id",
				"createRule": "",
				"updateRule": "id = @request.auth.id",
				"deleteRule": "id = @request.auth.id",
				"options": {
					"allowEmailAuth": true,
					"allowOAuth2Auth": true,
					"allowUsernameAuth": true,
					"exceptEmailDomains": null,
					"manageRule": null,
					"minPasswordLength": 8,
					"onlyEmailDomains": null,
					"onlyVerified": false,
					"requireEmail": false
				}
			},
			{
				"id": "ish6dryljtbzwok",
				"created": "2024-05-15 06:58:59.472Z",
				"updated": "2024-05-15 07:08:57.622Z",
				"name": "products",
				"type": "base",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "v1isddhf",
						"name": "name",
						"type": "text",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "qy4d2ayv",
						"name": "description",
						"type": "text",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "xxviudim",
						"name": "price",
						"type": "number",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"noDecimal": false
						}
					},
					{
						"system": false,
						"id": "edggzzbs",
						"name": "stockquantity",
						"type": "number",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"noDecimal": false
						}
					},
					{
						"system": false,
						"id": "zvtbh1lc",
						"name": "category",
						"type": "text",
						"required": false,
						"presentable": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					}
				],
				"indexes": [],
				"listRule": "",
				"viewRule": null,
				"createRule": null,
				"updateRule": null,
				"deleteRule": null,
				"options": {}
			}
		]`

		collections := []*models.Collection{}
		if err := json.Unmarshal([]byte(jsonData), &collections); err != nil {
			return err
		}

		err := daos.New(db).ImportCollections(collections, true, nil)
		if err != nil {
			return err
		}

		// Insert test data
		_, err = db.NewQuery("INSERT INTO products (name, description, price, stockquantity, category) VALUES\n('Widget A', 'A useful widget', 19.99, 100, 'Widgets'),\n('Widget B', 'Another useful widget', 25.99, 150, 'Widgets'),\n('Gadget A', 'A nifty gadget', 29.99, 200, 'Gadgets'),\n('Gadget B', 'Another nifty gadget', 35.99, 90, 'Gadgets'),\n('Tool A', 'An indispensable tool', 9.99, 80, 'Tools'),\n('Tool B', 'Another indispensable tool', 14.99, 120, 'Tools'),\n('Device A', 'A vital device', 199.99, 40, 'Devices'),\n('Device B', 'Another vital device', 249.99, 50, 'Devices'),\n('Appliance A', 'A necessary appliance', 79.99, 75, 'Appliances'),\n('Appliance B', 'Another necessary appliance', 89.99, 65, 'Appliances'),\n('Gizmo A', 'A handy gizmo', 4.99, 200, 'Gizmos'),\n('Gizmo B', 'Another handy gizmo', 6.99, 300, 'Gizmos'),\n('Thingamajig A', 'A useful thingamajig', 1.99, 500, 'Thingamajigs'),\n('Thingamajig B', 'Another useful thingamajig', 2.99, 600, 'Thingamajigs'),\n('Doodad A', 'A necessary doodad', 0.99, 700, 'Doodads'),\n('Doodad B', 'Another necessary doodad', 1.49, 800, 'Doodads'),\n('Contraption A', 'A complex contraption', 99.99, 30, 'Contraptions'),\n('Contraption B', 'Another complex contraption', 109.99, 20, 'Contraptions'),\n('Gimmick A', 'An interesting gimmick', 39.99, 110, 'Gimmicks'),\n('Gimmick B', 'Another interesting gimmick', 44.99, 120, 'Gimmicks');").Execute()

		return err
	}, func(db dbx.Builder) error {
		return nil
	})
}
