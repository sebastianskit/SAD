

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;

public class EditableBufferedReader extends BufferedReader {

    public EditableBufferedReader(Reader in) {
        
        super(in);
       
        //modificar el reader que ens pasen . 
    }

    @Override
    public int read() throws IOException {
       
        return super.read();  
    }
}