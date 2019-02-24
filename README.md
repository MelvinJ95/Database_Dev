# GramChat 

The Gramchat API is based on a database application for photo messaging in a social context, like Instagram but based on chat groups. The data in the application is managed by a relational database system, and exposed to the
client applications through a REST API.


The application is organized in three broad layers:

 1)Main - the main app module takes care to setup the routes for the REST API and calling the proper handler objects to process the request.
 
 2)Handlers - the handler modules takes care of implementing the logic of each REST call. In this sense, a handler is a Facade for accessing a given operation on a data collection. Each object handles a particular type of request for a data collection (e.g. Parts). The handlers rely upon the Data Access Objects (DAOs) to extact data from the database. The handlers encode the responses to the client with JSON and provide the appropriate HTTP response code.
 
 3)DAOs - the Data Access Objects (DAOs) take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropriate types.


