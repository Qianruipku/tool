#ifndef FUNCTION_H
#define FUNCTION_H
#include <vector>
using namespace std;
class FUNC
{
    public:
        //convert between different units
        void unitcovert();
    private:
        void convertT();
    
    public:
        //calculate md parameters with temperature, density and natom
        void mdparameter();
    private:
        //calculate chemical potential of free electron gas
        double FEG_mu(const double density_e_bohr, const double T_eV);
        //estimate ECUT with FEG model
        double FEG_ECUT1(double mu, double T);
        double FEG_ECUT2(double mu, double T);

    public:
        //calculate transport coefficients
        void conductivity();
    private:
        void lee_more(const double T_eV, const double mu_eV, const double density_e, 
                        const vector<double>& denlist_i, const vector<double>& zlist);

    public:
        //read
        double read_density();
        double read_temperature();
        double read_number_of_molecules();
        double read_elemets(vector<double> &mlist, vector<double> &zlist, vector<double> &nlist);
};
#endif
