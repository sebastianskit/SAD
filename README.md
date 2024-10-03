MVC desacopla els tres elements: podem cambiar la vista.
El model modifica la vista dels seus canvis, actualitzant la seva presentació. 
El model no te perquè conèixer els detalls de la vista/vistes.

*Patro observar/observable*
Els observers (vistes) es registren amb el observable (model).
El model informa les vistes amb notifyObservers quan el seu estat canvia.  
Internament manté una llista d'observers registrats . 
notiifyObservers invoca update de cada vista per actualitzar-la

class Observable {
    void addObserver (Observer o);
    void notifyObservers (); //pull model
    void notifyObservers (Object arg) //push model
    void  setChanged();
}
interfaceObservar{
    void update (Observable o, Object arg);
}