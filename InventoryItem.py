import grpc
import inventory_pb2
import inventory_pb2_grpc
class InventoryItem:
    def __init__(self, sku, description, bin_number, location, unit, qty, reorder_qty, cost):
        self.sku = sku
        self.description = description
        self.bin_number = bin_number
        self.location = location
        self.unit = unit
        self.qty = qty
        self.reorder_qty = reorder_qty
        self.cost = cost

    def to_proto(self):
        # Convert InventoryItem instance to a gRPC message (InventoryRecord)
        inventory_record = inventory_pb2.InventoryRecord(
            sku=self.sku,
            description=self.description,
            bin_number=self.bin_number,
            location=self.location,
            unit=self.unit,
            qty=self.qty,
            reorder_qty=self.reorder_qty,
            cost=self.cost
        )
        return print(inventory_record)

    def __str__(self):
        return f"SKU: {self.sku}, Description: {self.description}, Quantity: {self.qty}, Cost: ${self.cost:.2f}"