# Project Introduction
This project focuses on leveraging gRPC to streamline communication between client and server providers. The
five essential functions are SearchByID, SearchBySKU, SearchBySKURange, GetDistribution, and UpdateCost. It begins with
setting up a local connection and culminates in deploying the
server program to the cloud. Throughout this transition, the
client program interacts with the server provider.

##  SERVICE DEVELOPMENT
This service includes five gRPC methods: SearchByID,
SearchBySKU, SearchBySKURange, GetDistribution, and
UpdateCost.
1) SearchByIDRequest: Contains a single string field sku
for specifying the SKU for a search request.  
2) SearchBySKURequest: Includes two string fields, key_name and key_value, to filter records based on specific
keys.  
3) SearchBySKURangeRequest: Holds two string fields,
start-sku and end-sku, to define a range for SKU searches.  
4) GetDistributionRequest: Carries a double field percentile
to retrieve records based on a specified percentile of cost.  
5) UpdateCostRequest: Consists of a string new-sku, a double new-cost, and a boolean success field for updating
and indicating the success of cost changes.  
6) InventoryRecord: Describes the structure of an inventory
item with SKU, Description, Bin number, Location, Unit,
Quantity, Reorder Quantity, and Cost.  
7) InventoryRecordList: Similar to InventoryRecord but includes two additional fields, key-name and key-value, for
key-based searches.  
8) InventoryRangeList: Contains start-sku, end-sku, and sku
fields for specifying a range of SKUs.  
9) UpdateResponse: Defines the response structure for the
UpdateCost gRPC, including new-sku, new cost, and a
success indicator.  
