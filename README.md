# gp_dr12_trained

This repository contains the trained Gaussian Process (GP) models, catalog, and pre-computed Quasi-Monte Carlo samples used in [Ho-Bird-Garnett (2021)](https://arxiv.org/abs/2103.10964). This is the trained model based on SDSS DR12 spectra.

## Contents

The repository stores the following files, which are also publicly available [here](http://tiny.cc/multidla_catalog_gp_dr12q):

### Required `.mat` Files

1. **GP Model on Spectra Without DR9 Concordance DLAs (2003.11036)**  
   [learned_qso_model_lyseries_variance_kim_dr9q_minus_concordance.mat](https://drive.google.com/file/d/16n7cDNyXmwoHOw9jFiF5em1z8Q4hQkED/view?usp=sharing)

2. **GP Model Trained on Spectra Without Ho DR12 DLAs (2103.10964)**  
   [learned_qso_model_lyseries_variance_wmu_boss_dr16q_minus_dr12q_gp_851-1421.mat](https://drive.google.com/file/d/1R4KvOKzQe17SheEYY8Mc7ia6OErbTL6x/view?usp=sharing)

3. **DLA Samples for Quasi-Monte Carlo Integration**  
   [dla_samples_a03.mat](https://drive.google.com/file/d/1pE5nFkMvXPmSJimr6uXBRUWNYZhp9h00/view?usp=sharing)

4. **SubDLA Samples for Quasi-Monte Carlo Integration**  
   [subdla_samples.mat](https://drive.google.com/file/d/1UFdsFAiYNU8QdGph4UY3B86W-ge-112n/view?usp=sharing)

5. **SDSS DR12 QSO Catalogue (Including `filter_flags`)**  
   [catalog.mat](https://drive.google.com/file/d/1-DE6NdFhaEcI0bk-l-GiN2DzxoWoLW-L/view?usp=sharing)

### Catalog File

The `catalog.mat` file provided in this repository is a refined version of the original catalog, containing only the essential arrays needed for analysis. This reduces the file size and optimizes processing.

To generate this smaller version of the catalog, use the script `save_into_small.py`.

## Default parameters used for training the GP

```bash
% normalization parameters
normalization_min_lambda = 1425;              % range of rest wavelengths to use   Å
normalization_max_lambda = 1475;              %   for flux normalization

% null model parameters
min_lambda         =  850.75;                 % range of rest wavelengths to       Å
max_lambda         = 1420.75;                 %   model
dlambda            =    0.25;                 % separation of wavelength grid      Å
k                  = 20;                      % rank of non-diagonal contribution
max_noise_variance = 3^2;                     % maximum pixel noise allowed during model training

% optimization parameters
initial_c_0   = 0.1;                          % initial guess for c₀
initial_tau_0 = 0.00554;                      % initial guess for τ₀
initial_beta  = 3.182;                        % initial guess for β
minFunc_options =               ...           % optimization options for model fitting
    struct('MaxIter',     2000, ...
           'MaxFunEvals', 4000);

% DLA model parameters: parameter samples
num_dla_samples     = 10000;                  % number of parameter samples
alpha               = 0.97;                   % weight of KDE component in mixture
uniform_min_log_nhi = 20.0;                   % range of column density samples    [cm⁻²]
uniform_max_log_nhi = 23.0;                   % from uniform distribution
fit_min_log_nhi     = 20.0;                   % range of column density samples    [cm⁻²]
fit_max_log_nhi     = 22.0;                   % from fit to log PDF
```

