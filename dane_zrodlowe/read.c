
/* *******************************************************
 * This sample code shows how to read binary data
 * from psi.dat
 *
 *
 * Author:
 *   Gabriel Wlazlowski <gabrielw@if.pw.edu.pl>
 *
 * INFO:
 * Units - natural units: m=\hbar=dx=1
 *
 * Compile command:
 * gcc read.c -o read -lm
 * *******************************************************/

#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <complex.h>

int main( int argc , char ** argv )
{
    int nx, ny, nz; // lattice size
    double dx, dy, dz; // lattice spacing in each direaction, should be dx=dy=dz=1
    double eF; // Fermi energy - reference energy
    double t0, dt; // value of time and time step - IGNORE
    int nom; // number of records - should be nom=1 - IGNORE

    FILE *infile = fopen("psi.dat", "rb");

    fseek(infile, sizeof( int ), SEEK_SET); // skip first integer - info about precision of data
    fread(&nx, sizeof( int ), 1, infile);
    fread(&ny, sizeof( int ), 1, infile);
    fread(&nz, sizeof( int ), 1, infile);
    fread(&dx, sizeof( double ), 1, infile);
    fread(&dy, sizeof( double ), 1, infile);
    fread(&dz, sizeof( double ), 1, infile);
    fread(&eF, sizeof( double ), 1, infile);
    fread(&t0, sizeof( double ), 1, infile);
    fread(&dt, sizeof( double ), 1, infile);
    fread(&nom, sizeof( int ), 1, infile);

    // printf("# Lattice size: %d x %d x %d (with lattice spacing %.1f x %.1f x %.1f)\n", nx, ny, nz, dx, dy, dz);

    // Allocate momory for psi
    double complex *psi;
    if ( ( psi = (double complex *) malloc( (nx*ny*nz) * sizeof( double complex ) ) ) == NULL )
    {                                                                           \
        printf("Cannot allocate memory!\n");
        return( EXIT_FAILURE ) ;
    }

    // Read data
    if( fread(psi, sizeof( double complex ), nx*ny*nz, infile) != nx*ny*nz )
    {
        printf("Cannot read data!\n");
        return( EXIT_FAILURE ) ;
    }

    // close file
    fclose(infile);

    // EXAMPLE: compute particle number and print density along z axis
    // N = \int |\psi(r)|^2 dr
    double npart=0.0;
    double rho;
    int ix, iy, iz, ixyz;
    for(ix=0; ix<nx; ix++) for(iy=0; iy<ny; iy++) for(iz=0; iz<nz; iz++)
    {
        ixyz=iz + iy*nz + ix*ny*nz;
        rho = pow(cabs(psi[ixyz]), 2); // compute density
        npart += rho;

        // if(ix==nx/2 && iy==ny/2)
            // printf("%6d %12.6g\n", iz, rho);
        // printf("%12.6g\n", rho);
        printf("%12.6g %12.6g\n", creal(psi[ixyz]), cimag(psi[ixyz]));
    }

    // printf("# Number of particles= %f\n", npart);

    // clear memory
    free(psi);

    return( EXIT_SUCCESS ) ;
}
