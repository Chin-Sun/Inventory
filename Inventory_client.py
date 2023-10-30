import grpc
import inventory_pb2
import inventory_pb2_grpc
import time

def main():
    channel = grpc.insecure_channel('inventoryservice1.azurewebsites.net:50052')
    stub = inventory_pb2_grpc.InventoryServiceStub(channel)

    while True:
        print("Client Menu:")
        print("1. Search by SKU ID")
        print("2. Search by Key Pairs(only accept sku, description)")
        print("3. Search by SKU Range")
        print("4. Get Distribution by Percentile")
        print("5. Update Cost")
        choice = input("Enter your choice: ")

        if choice == "1":
            sku = input("Enter SKU ID: ")
            request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
            # Initialize lists to store delay times
            delays = []
            i = 1
            # Run the client 100 times
            for i in range(100):
                start_time = time.time()
                # Make a gRPC request
                request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
                end_time = time.time()
                delay = end_time - start_time
                delays.append(delay)
            # Calculate mean and standard deviation
            print(delay)
            mean_delay = sum(delays) / len(delays)
            std_delay = (sum((x - mean_delay) ** 2 for x in delays) / len(delays)) ** 0.5
            print(mean_delay, std_delay)

        elif choice == "2":
            key_name = input("Enter Key Name: ")
            key_value = input("Enter Key Value: ")
            request = stub.SearchBySKU(inventory_pb2.SearchBySKURequest(key_name=key_name, key_value=key_value))

            # Initialize lists to store delay times
            delays = []
            i = 1
            # Run the client 100 times
            for i in range(100):
                start_time = time.time()
                # Make a gRPC request
                request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
                end_time = time.time()
                delay = end_time - start_time
                delays.append(delay)
            # Calculate mean and standard deviation
            print(delay)
            mean_delay = sum(delays) / len(delays)
            std_delay = (sum((x - mean_delay) ** 2 for x in delays) / len(delays)) ** 0.5
            print(mean_delay, std_delay)

        elif choice == "3":
            start_sku = input("Enter start SKU: ")
            end_sku = input("Enter end SKU: ")
            request = stub.SearchBySKURange(inventory_pb2.SearchBySKURangeRequest(start_sku=start_sku, end_sku=end_sku))

            # Initialize lists to store delay times
            delays = []
            i = 1
            # Run the client 100 times
            for i in range(100):
                start_time = time.time()
                # Make a gRPC request
                request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
                end_time = time.time()
                delay = end_time - start_time
                delays.append(delay)
            # Calculate mean and standard deviation
            print(delay)
            mean_delay = sum(delays) / len(delays)
            std_delay = (sum((x - mean_delay) ** 2 for x in delays) / len(delays)) ** 0.5
            print(mean_delay, std_delay)

        elif choice == "4":
            percentile = float(input("Enter percentile (e.g., 0.5 for 50%): "))
            request = stub.GetDistribution(inventory_pb2.GetDistributionRequest(percentile=percentile))

            # Initialize lists to store delay times
            delays = []
            i = 1
            # Run the client 100 times
            for i in range(100):
                start_time = time.time()
                # Make a gRPC request
                request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
                end_time = time.time()
                delay = end_time - start_time
                delays.append(delay)
            # Calculate mean and standard deviation
            print(delay)
            mean_delay = sum(delays) / len(delays)
            std_delay = (sum((x - mean_delay) ** 2 for x in delays) / len(delays)) ** 0.5
            print(mean_delay, std_delay)

        elif choice == "5":
            new_sku = input("Enter SKU: ")
            new_cost= float(input("Enter new COST: "))
            request = stub.UpdateCost(inventory_pb2.UpdateCostRequest(new_sku=new_sku, new_cost=new_cost))

            # Initialize lists to store delay times
            delays = []
            i = 1
            # Run the client 100 times
            for i in range(100):
                start_time = time.time()
                # Make a gRPC request
                request = stub.SearchByID(inventory_pb2.SearchByIDRequest(sku=sku))
                end_time = time.time()
                delay = end_time - start_time
                delays.append(delay)
            # Calculate mean and standard deviation
            print(delay)
            mean_delay = sum(delays) / len(delays)
            std_delay = (sum((x - mean_delay) ** 2 for x in delays) / len(delays)) ** 0.5
            print(mean_delay, std_delay)


if __name__ == '__main__':
    main()
