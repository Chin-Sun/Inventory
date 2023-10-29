import grpc
import inventory_pb2
import inventory_pb2_grpc
from InventoryItem import InventoryItem
from concurrent import futures


class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    inventory_data = {
                                  "SP7875": InventoryItem(
                                      sku="SP7875",
                                      description="Item 1",
                                      bin_number="T345",
                                      location="Row 2, slot 1",
                                      unit="Each",
                                      qty=20,
                                      reorder_qty=10,
                                      cost=30.00
                                  ),
                                  "TR87680": InventoryItem(
                                      sku="TR87680",
                                      description="Item 2",
                                      bin_number="T345",
                                      location="Row 2, slot 1",
                                      unit="Each",
                                      qty=30,
                                      reorder_qty=15,
                                      cost=40.00
                                  ),
                                  "MK676554": InventoryItem(
                                      sku="MK676554",
                                      description="Item 3",
                                      bin_number="T5789",
                                      location="Row 1, slot 1",
                                      unit="Each",
                                      qty=10,
                                      reorder_qty=5,
                                      cost=5.00
                                  ),
                                  "YE98767": InventoryItem(
                                      sku="YE98767",
                                      description="Item 4",
                                      bin_number="T9876",
                                      location="Row 3, slot 2",
                                      unit="Box (10 ct)",
                                      qty=40,
                                      reorder_qty=10,
                                      cost=15.00
                                  ),
                                  "XR23423": InventoryItem(
                                      sku="XR23423",
                                      description="Item 5",
                                      bin_number="T098",
                                      location="Row 3, slot 1",
                                      unit="Each",
                                      qty=12,
                                      reorder_qty=10,
                                      cost=26.00
                                  ),
                                  "PW98762": InventoryItem(
                                      sku="PW98762",
                                      description="Item 6",
                                      bin_number="T345",
                                      location="Row 2, slot 1",
                                      unit="Each",
                                      qty=7,
                                      reorder_qty=10,
                                      cost=50.00
                                  ),
                                  "BM87684": InventoryItem(
                                      sku="BM87684",
                                      description="Item 7",
                                      bin_number="T349",
                                      location="Row 1, slot 2",
                                      unit="Each",
                                      qty=10,
                                      reorder_qty=5,
                                      cost=10.00
                                  ),
                                  "BH67655": InventoryItem(
                                      sku="BH67655",
                                      description="Item 8",
                                      bin_number="T5789",
                                      location="Row 1, slot 1",
                                      unit="Each",
                                      qty=19,
                                      reorder_qty=10,
                                      cost=3.00
                                  ),
                                  "WT98768": InventoryItem(
                                      sku="WT98768",
                                      description="Item 9",
                                      bin_number="T9875",
                                      location="Row 2, slot 2",
                                      unit="Package (5 ct)",
                                      qty=20,
                                      reorder_qty=30,
                                      cost=14.00
                                  ),
                                  "TS3456": InventoryItem(
                                      sku="TS3456",
                                      description="Item 10",
                                      bin_number="T349",
                                      location="Row 1, slot 2",
                                      unit="Each",
                                      qty=15,
                                      reorder_qty=8,
                                      cost=60.00
                                  ),
                                  "WDG123": InventoryItem(
                                      sku="WDG123",
                                      description="Item 11",
                                      bin_number="T349",
                                      location="Row 1, slot 2",
                                      unit="Each",
                                      qty=25,
                                      reorder_qty=15,
                                      cost=8.00
                                  ),

        }

    def calculate_inventory_value(self, item):
        return item.qty * item.cost

    def SearchByID(self, request, context):
        print("SearchByID Request Made:")
        print(request)
        sku = request.sku
        item = InventoryService.inventory_data.get(sku)
        if item is not None:
            response=inventory_pb2.InventoryRecord(
                sku=item.sku,
                description=item.description,
                bin_number=item.bin_number,
                location=item.location,
                unit=item.unit,
                qty=item.qty,
                reorder_qty=item.reorder_qty,
                cost=item.cost,
            )
            print(f"SKU: {response.sku}, Description: {response.description}, "
                  f"Bin#:{response.bin_number}, Location:{response.location}, "
                  f"QTY:{response.qty}, Reorder QTY:{response.reorder_qty}, Cost: {response.cost}")
            return response
        else:
            return None  # You might need to handle None differently depending on your proto definition

    def SearchBySKU(self, request, context):
        print("SearchByKey_Pairs Request Made:")
        # print(request)
        key_name = request.key_name
        key_value = request.key_value
        for sku, item in self.inventory_data.items():
         if key_name =="sku" and item.sku == key_value:
             item = InventoryService.inventory_data.get(sku)
             request = inventory_pb2.InventoryRecord(
                 sku=item.sku,)
             print(f"SKU: {request.sku}")
             return request
         elif key_name == "description" and item.description == key_value:
             item = InventoryService.inventory_data.get(sku)
             request = inventory_pb2.InventoryRecord(
                      sku=item.sku,
                      description=item.description,
             )
             print(f"SKU: {request.sku}, Description: {request.description}")
             return request

    def SearchBySKURange(self, request, context):
        print("SearchBySKURange Request Made:")
        print(request)
        sku_list = ["SP7875", "TR87680", "MK676554", "YE98767", "XR23423", "PW98762", "BM87684", "BH67655",
                       "WT98768", "TS3456", "WDG123"]
        start_sku = request.start_sku
        end_sku = request.end_sku
        index_start = sku_list.index(start_sku)
        index_end = sku_list.index(end_sku)
        if index_start < index_end:
                result = sku_list[index_start:index_end + 1]
                for i in range(index_start, index_end + 1):
                  request = inventory_pb2.InventoryRangeList(sku=result[i])
                  print(f"SKU: {request.sku}")
                  yield request
        else:
                print("The index of the first value should be before the second value")


    def GetDistribution(self, request, context):
        print("GetDistribution Request Made:")
        print(request)
        percentile = request.percentile
        cost_list = [item.cost for item in InventoryService.inventory_data.values()]
        cost_list.sort()
        index = int(len(cost_list) * percentile)
        distribution_items = [item for item in InventoryService.inventory_data.values() if item.cost == cost_list[index]]
        for item in distribution_items:
            item.inventory_value = self.calculate_inventory_value(item)
            request = inventory_pb2.InventoryRecordList(
                sku=item.sku,
                description=item.description,
                bin_number=item.bin_number,
                location=item.location,
                unit=item.unit,
                qty=item.qty,
                reorder_qty=item.reorder_qty,
                cost=item.cost,
            )
            print(f"SKU: {request.sku}, Description: {request.description}, "
                  f"Bin#:{request.bin_number}, Location:{request.location}, "
                  f"QTY:{request.qty}, Reorder QTY:{request.reorder_qty}, Cost: {request.cost}")

        return request

    def UpdateCost(self, request, context):
        print("UpdateCost Request Made:")
        print(request)
        new_sku = request.new_sku
        new_cost = request.new_cost
        success = False
        for sku, item in self.inventory_data.items():
            if sku == new_sku:
                item.cost = new_cost
                success = True
                print(f"SKU: {item.sku}, New Cost: {item.cost}")

        return inventory_pb2.UpdateResponse(success=success)


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run_server()
