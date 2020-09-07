import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ClientService {
  constructor(private http: HttpClient) {}

  // tslint:disable-next-line: typedef
  getRequest(route: string, token?: string, strQuery?: string) {
    const config: any = {
      responseType: 'json',
    };
    if (token) {
      const header = new HttpHeaders().set('Authorization', `Bearer ${token}`);
      config.headers = header;
      console.log(token);
    }
    if (strQuery) {
      const params = new HttpParams().set('lineMobile', `${strQuery}`);
      config.params = params;
    }
    return this.http.get(route, config);
  }

  // tslint:disable-next-line: typedef
  postRequest(route: string, data?: any, token?: string) {
    const config: any = {
      responseType: 'json',
    };
    if (token) {
      const header = new HttpHeaders().set('Authorization', `Bearer ${token}`);
      config.headers = header;
      console.log(token);
    }
    return this.http.post(route, data, config);
  }
  // tslint:disable-next-line: typedef
  putRequest(route: string, data?: any, token?: string) {
    const config: any = {
      responseType: ' json',
    };
    if (token) {
      const header = new HttpHeaders().set('Authorization', `Bearer ${token}`);
      config.headers = header;
      console.log(token);
    }
    return this.http.put(route,data, config);
  }
}
