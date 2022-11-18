String EncodedString = "url+decode";
String DecodedString = Server.UrlDecode( EncodedString );
Response.Write( "http://example.com/?param=" + DecodedString );
