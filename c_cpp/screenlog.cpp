#include <iostream>
#include <string>




struct Colours
{
	static const std::string RED;
	static const std::string GREEN;
	static const std::string YELLOW;
	static const std::string NOCOL;
};
const std::string Colours::RED    = "\e[31m";
const std::string Colours::GREEN  = "\e[32m";
const std::string Colours::YELLOW = "\e[33m";
const std::string Colours::NOCOL  = "\e[0m";



class ColourScreenlogger
{
public:
	ColourScreenlogger(std::ostream& os) : _holder(Holder(os)) {}
	ColourScreenlogger(std::ostream& os, const std::string& start, const std::string& col) : _holder(Holder(os, start, col)) {}
	
	//~ template <class T>
	//~ friend std::ostream& operator<< (const ColourScreenlogger& l, const T& t)
	//~ {
		//~ return (l._holder._os) << t;
	//~ }
	friend std::ostream& operator<< (const ColourScreenlogger& l, const std::string& t)	{ return (l._holder._os) << t; }
	friend std::ostream& operator<< (const ColourScreenlogger& l, const char* t)      	{ return (l._holder._os) << t; }
	friend std::ostream& operator<< (const ColourScreenlogger& l, const int t)        	{ return (l._holder._os) << t; }
	friend std::ostream& operator<< (const ColourScreenlogger& l, const double t)        	{ return (l._holder._os) << t; }

private:
	struct Holder {
		Holder (std::ostream& os) : _os(os) { _os << Colours::NOCOL; }
		Holder (std::ostream& os, const std::string& start, const std::string& col) : _os(os) { _os << col << "[" << start << "]" << "\t"; }
		~Holder () { _os << Colours::NOCOL << std::endl; }
		
		std::ostream& _os;
	};
	
	Holder _holder;
};



ColourScreenlogger wrap(std::ostream& os)
{
	return ColourScreenlogger(os);
}

ColourScreenlogger logn(const std::string& start) { return ColourScreenlogger(std::cerr, start, Colours::NOCOL); }
ColourScreenlogger logr(const std::string& start) { return ColourScreenlogger(std::cerr, start, Colours::RED);   }
ColourScreenlogger logg(const std::string& start) { return ColourScreenlogger(std::cerr, start, Colours::GREEN); }
ColourScreenlogger logy(const std::string& start) { return ColourScreenlogger(std::cerr, start, Colours::YELLOW);}



using namespace std;


int main(int argc, char* argv[])
{

	logn(__func__) << "Hello" << " Hello" << " NOCOL";
	cout << "noncoloured cout" << endl;
	wrap(std::cout) << "Hello" << " Hello" << " NOCOL wrap";
	logr(__func__) << "Hello" << " Hello" << " RED " << 10;
	cout << "noncoloured cout" << endl;
	wrap(std::cout) << "Hello" << " Hello" << " NOCOL wrap";
	logg(__func__) << "Hello" << " Hello" << " GREEN " << 10.01;
	cout << "noncoloured cout" << endl;
	wrap(std::cout) << "Hello" << " Hello" << " NOCOL wrap";
	logy(__func__) << "Hello" << " Hello" << " YELLOW";
	cout << "noncoloured cout" << endl;
	wrap(std::cout) << "Hello" << " Hello" << " NOCOL wrap";

	return 0;
}
