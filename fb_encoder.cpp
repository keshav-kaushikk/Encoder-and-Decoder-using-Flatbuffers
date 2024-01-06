
#include <iostream>
#include <fstream>
#include "client_data_generated.h" // includes "flatbuffers/flatbuffers.h"

using namespace Clnt;

int main()
{
	
	flatbuffers::FlatBufferBuilder builder;

	//Serializing Clients

    //Client 1	
	auto client_one_name = builder.CreateString("Ram");
	short client_one_age = 21;
	float client_one_weight = 76.5;
	bool client_one_gender = 0; // 0 for Male, 1 for Female

    //Creating Client 1
	auto client_one_person = CreatePerson(builder, client_one_age, client_one_weight, client_one_gender);
	auto client_one = CreateClient(builder, client_one_name, Client_Type_Person, client_one_person.Union());

	//Client 2	
	auto client_two_name = builder.CreateString("Fight Club");
	float client_two_age = 24.5;
	float client_two_weight = 66;

    auto participant1 = builder.CreateString("Ram");
    auto participant2 = builder.CreateString("Shyam");
    auto participant3 = builder.CreateString("Raghuveer");

	std::vector<flatbuffers::Offset<flatbuffers::String>> client_two_participant_namelist;
    client_two_participant_namelist.push_back(participant1);
    client_two_participant_namelist.push_back(participant2);
    client_two_participant_namelist.push_back(participant3);
    auto client_two_participants = builder.CreateVector(client_two_participant_namelist);

    //Creating Client 2
    auto client_two_group = CreateGroup(builder, client_two_age, client_two_weight, client_two_participants);
    auto client_two = CreateClient(builder, client_two_name, Client_Type_Group, client_two_group.Union());


    // Serializing "Clients" vector
    std::vector<flatbuffers::Offset<Client>> clients_vector;
	clients_vector.push_back(client_one);
	clients_vector.push_back(client_two);

    //Creating "Clients" vector
	auto clients_fbv = builder.CreateVector(clients_vector);	
	auto clients = CreateClients(builder, clients_fbv);

    //Finishing the buffer
					
	builder.Finish(clients);

	std::cout<<"\nBuffers created!!";
	
	//Preparing to write to file
	auto clients_ptr = builder.GetBufferPointer();
	auto size = builder.GetSize();
	
	//Dumping File
	std::ofstream bin_file;
	bin_file.open("bin/fb_bytes.bin", std::ios::binary);
	
	if(!bin_file) {
		std::cout<<"\nOpening File Failed!!";
	}

	else {
		bin_file.write((char*)clients_ptr, size);
		bin_file.close();
	}

	return 0;
}